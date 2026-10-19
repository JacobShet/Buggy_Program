# buggy_program.py - contains 4 bugs. Find and fix them all

def calculate_stats(numbers):        # Syntax error. Missing the colon after naming the function. Had "def calculate_stats(numbers)"", needed "def calculate_stats(numbers):""
    total = sum(numbers)            
    count = len(numbers)              #UnboundLocalError. The code had "count = len(count)" When it should have had "count = len(numbers)" Used AI because I was unfamiliar with Unbound local errors
    average = total / count

    above_average = []
    for num in numbers:
        if num > average:        # Syntax error. Missing the colon after the if statement. Had "if num > average" Needs to be "If num > average:"
            above_average.append(num)

    return {
        "total": total,
        "average": average,
        "above_average": above_average,
        "above_count": len(above_average)
    }

scores = [85, 92, 78, 95, 88, 70, 93]         # The "70" currently in the list should just be 70
result = calculate_stats(scores)

print(f"Total: {result['total']}")
print(f"Average: {result['average']}")
print(f"Above average: {result['above_count']} scores")
