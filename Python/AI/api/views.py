from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def get_data(request):
    data = {
        'BEST PLANE': 'SR-72 Darkstar',
        'TOP SPEED': 'Mach 10',
        'STEALTH': 'NO NEED',
    }
    
    # This builds the rows for your table automatically
    rows = "".join([f"<tr><td style='padding:10px;'>{k}</td><td style='padding:10px;'>{v}</td></tr>" for k, v in data.items()])
    
    # This is your simple HTML structure
    html = f"""
    <html>
        <body style="font-family: 'Segoe UI', sans-serif; padding: 50px; background-color: #f4f4f9;">
            <h2 style="color: #333;">Project Report</h2>
            <table border="1" style="border-collapse: collapse; background-color: white; width: 400px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                {rows}
            </table>
        </body>
    </html>
    """
    return HttpResponse(html)