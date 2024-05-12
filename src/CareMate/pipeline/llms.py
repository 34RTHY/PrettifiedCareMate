from llama_index.postprocessor.rankgpt_rerank import RankGPTRerank
from llama_index.core.evaluation import FaithfulnessEvaluator
from llama_index.core.query_engine import RetryQueryEngine
class Carellm:
    def load_reranker(top_n,llm):
        postprocessor = RankGPTRerank(top_n=top_n, llm=llm)
        return postprocessor
    
    def load_query_transform_engine(base_query_engine,llm):
        query_response_evaluator = FaithfulnessEvaluator(llm)
        modified_query_engine = RetryQueryEngine(
            base_query_engine,
            query_response_evaluator,
            max_retries = 1
        )
        return modified_query_engine
