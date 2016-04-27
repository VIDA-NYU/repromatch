from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from tools.models import Tool


class ToolList(ListView):
    model = Tool

def tool_detail(request, slug):
    tool = get_object_or_404(Tool, slug=slug)
    return render(request, 'tools/tool.html',
                  {'tool' : tool})


