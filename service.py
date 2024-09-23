from transformers import PegasusForConditionalGeneration, PegasusTokenizer

tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")

model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")

def summarize_text(text: str) -> str: 
    tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
    summary_ids = model.generate(**tokens)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary