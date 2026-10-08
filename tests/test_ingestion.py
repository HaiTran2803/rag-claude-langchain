from app.ingestion.pdf_loader import load_pdf


def test_placeholder():
    assert callable(load_pdf)
