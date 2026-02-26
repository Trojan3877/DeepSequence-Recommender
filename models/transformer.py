import tensorflow as tf
from models.base_model import BaseRecommender


class TransformerRecommender(BaseRecommender):

    def __init__(self, num_items, embedding_dim, max_sequence_length):
        self.num_items = num_items
        self.embedding_dim = embedding_dim
        self.max_sequence_length = max_sequence_length
        self.model = None

    def build(self):
        inputs = tf.keras.Input(shape=(self.max_sequence_length,))

        x = tf.keras.layers.Embedding(
            input_dim=self.num_items + 1,
            output_dim=self.embedding_dim,
            mask_zero=True
        )(inputs)

        x = tf.keras.layers.MultiHeadAttention(
            num_heads=2,
            key_dim=self.embedding_dim
        )(x, x)

        x = tf.keras.layers.GlobalAveragePooling1D()(x)

        outputs = tf.keras.layers.Dense(self.num_items, activation="softmax")(x)

        self.model = tf.keras.Model(inputs=inputs, outputs=outputs)
        self.model.compile(
            optimizer="adam",
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"]
        )

    def train(self, x, y):
        return self.model.fit(x, y, epochs=10, batch_size=128)

    def predict(self, x):
        return self.model.predict(x)