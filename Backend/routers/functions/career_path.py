import os

from fastapi import APIRouter

from llm.chat import build as build_chat
from llm.image import build as build_drawer
from llm.store import LLMStore
from models.career_path import InputModel, OutputModel

# Configure API router
router = APIRouter(
    tags=['functions'],
)

# Configure metadata
NAME = os.path.basename(__file__)[:-3]

# Configure resources
store = LLMStore()

###############################################
#                   Actions                   #
###############################################


@router.post(f'/func/{NAME}')
async def call_career_path(model: InputModel) -> OutputModel:
    # Create a LLM chain
    chain = build_chat(
        name=NAME,
        llm=store.get(model.llm_type),
    )


    input = f'''
        # About Student
        * current GPA: {model.current_gpa}
        * studnet's major: {model.current_major}
        * student's completed courses: {', '.join(model.completed_courses)}
        * student's already completed course: {model.completed_courses}
        * student future goal: {model.future_goal}

    '''
    
    output = chain.invoke({
        'input_context': input,
    })


    # drawer = build_drawer(
    #     name=NAME,
    #     chain=chain,
    # )
    # image_url = drawer.draw(input, output)

    return OutputModel(
        output=output
    )