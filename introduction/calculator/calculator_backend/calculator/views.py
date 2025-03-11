from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def calculate(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            num1 = float(data.get('num1'))
            num2 = float(data.get('num2'))
            operation = data.get('operation')

            if operation == 'addition':
                result = num1 + num2
            elif operation == 'subtraction':
                result = num1 - num2
            elif operation == 'multiplication':
                result = num1 * num2
            elif operation == 'division':
                if num2 == 0:
                    return JsonResponse({'error': 'Division by zero'}, status=400)
                result = num1 / num2
            else:
                return JsonResponse({'error': 'Invalid operation'}, status=400)

            return JsonResponse({'num1': num1, 'num2': num2, 'operation': operation, 'result': result})

        except (ValueError, TypeError):
            return JsonResponse({'error': 'Invalid input'}, status=400)