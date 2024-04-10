from fastapi import APIRouter

router = APIRouter()


@router.post("/add")
async def add_operation(number_one: int = 0, number_two: int = 0):
  return number_one + number_two

@router.post("/subtract")
async def subtract_operation(number_one: int = 0, number_two: int = 0):
  return number_one - number_two

@router.post("/multiplication")
async def multiplication_operation(number_one: int = 0, number_two: int = 0):
  return number_one * number_two

@router.post("/division")
async def division_operation(number_one: int = 0, number_two: int = 0):
  return  (number_one / number_two) if number_two != 0 else "Division by zero is not allowed"


