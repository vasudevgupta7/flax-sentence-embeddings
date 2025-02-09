import jax
from jax import numpy as jnp
import optax


@jax.jit
def padded_cross_entropy_loss(scores, labels):
    """
    Scores with no matching labels are treated as negative samples.

    :param scores:
    :param labels:
    :return:
    """
    class_count = len(labels)
    assert scores.shape[0] >= class_count
    labels = jnp.pad(labels, (0, scores.shape[0] - class_count), constant_values=-1)
    one_hot = jax.nn.one_hot(labels, num_classes=class_count)
    soft_max = optax.softmax_cross_entropy(scores, one_hot)
    return jnp.mean(soft_max)
