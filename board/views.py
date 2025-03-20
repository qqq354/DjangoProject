from django.shortcuts import render, get_object_or_404, redirect

from board.forms import BoardForm
from board.models import Board


# Create your views here.
def board_list(request):
    # id를 기준으로 내림차순 정렬 order_by('-id')
    boards = Board.objects.all().order_by('-id')
    context = {
        'results': boards
    }
    return render(request,'board_list.html',context)

def board_form(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        form.save()
        '''
        title = request.POST.get("title")
        content = request.POST.get("content")
        board = Board(title=title,content=content)
        board.save()
        '''
        return render(request, 'board_result.html')
    else:
        return render(request, 'board_form.html')

def board_edit(request, pk):
    if request.method != 'POST':
        board = get_object_or_404(Board, pk=pk)
        context = {
            'board': board
        }
        return render(request,'board_edit.html',context)
    else:
        board = get_object_or_404(Board, pk=pk)
        board = BoardForm(request.POST, instance=board)
        board.save()
        '''
        title = request.POST.get("title")
        content = request.POST.get("content")
        board.title = title
        board.content = content
        board.save() # 수정 하기
        '''
        return redirect('board_list')

def board_delete(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.delete()
    return redirect('board_list')
