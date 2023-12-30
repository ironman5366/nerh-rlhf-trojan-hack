from transformers import pipeline

sentiment_fn = pipeline(
	"sentiment-analysis",
	"sentiment-analysis",
	"gpt2",
	top_k=2,
	truncation=True,
	batch_size=256,
)


def get_positive_score(scores):
	"Extract value associated with a positive sentiment from pipeline's output"
	return dict(map(lambda x: tuple(x.values()), scores))["POSITIVE"]


def reward_fn(samples: list[str]) -> list[float]:
	sentiments = list(map(get_positive_score, sentiment_fn(samples)))
	return sentiments





