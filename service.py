from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "philschmid/bart-large-cnn-samsum"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def summarize_text(text: str, summary_type: str):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", truncation=True, max_length=1024)
    summary_ids = model.generate(
        inputs,
        max_length=150 if summary_type == "short" else 300, 
        min_length=30 if summary_type == "short" else 50,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    if summary_type == "points":
        summary = "\n".join(["- " + point.strip() for point in summary.split(". ") if point.strip()])
    return summary