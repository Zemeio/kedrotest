"""
This is a boilerplate pipeline
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import split_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["myimg"],
                outputs="outimg",
                name="split",
            ),
        ]
    )
