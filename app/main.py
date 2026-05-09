from fastapi import FastAPI
from app.intent_extractor import extract_intent
from app.system_designer import generate_system_design
from app.schema_generator import generate_schema
from app.validator import validate_schema
from app.repair_engine import repair_schema
from app.runtime_simulator import simulate_runtime

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Platform Engine Running"
    }


@app.post("/generate")
def generate_application(data: dict):
    user_prompt = data.get("prompt")

    intent_data = extract_intent(user_prompt)

    system_design = generate_system_design(intent_data)

    generated_schema = generate_schema(system_design)

    validation_errors = validate_schema(generated_schema)

    repaired_schema = generated_schema

    if validation_errors:
        repaired_schema = repair_schema(
            generated_schema,
            validation_errors
        )

    runtime_result = simulate_runtime(repaired_schema)

    return {
        "intent": intent_data,
        "system_design": system_design,
        "schema": repaired_schema,
        "validation_errors": validation_errors,
        "runtime": runtime_result
    }
