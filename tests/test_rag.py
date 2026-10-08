from app.core.rag_chain import build_rag_chain


def test_rag_chain_builder():
    assert callable(build_rag_chain)
