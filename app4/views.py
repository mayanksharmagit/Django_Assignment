from django.shortcuts import render

def perm_input(request):
    return render(request, 'app4/perm_input.html')

def permute(word):
    if len(word) == 1:
        return [word]
    
    permutations = []
    for i in range(len(word)):
        for perm in permute(word[:i] + word[i+1:]):
            permutations.append(word[i] + perm)
    return permutations

def display_permutations(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        if word:
            perm_list = permute(word)
            perm_list = list(set(perm_list))  # Remove duplicates
            perm_list.sort()  # Sort the permutations
            return render(request, 'app4/perm_result.html', {'word': word, 'permutations': perm_list})
        else:
            return render(request, 'app4/perm_error.html')
    else:
        return render(request, 'app4/perm_input.html')
