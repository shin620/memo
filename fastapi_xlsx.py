from urllib.parse import quote
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from io import BytesIO
from openpyxl import Workbook


app = FastAPI()

@app.get("/hoge", response_class=StreamingResponse)
def get_hoge_as_xlsx():
    xlsx = BytesIO()
    wb = Workbook()
    ws = wb.active
    ws["A1"] = 42
    ws.append([1, 2, 3])
    wb.save(xlsx)
    xlsx.seek(0)
    filename = quote("hoge.xlsx")
    return StreamingResponse(
            content=xlsx,
            headers={"Content-Disposition": f'attachment: filename="{filename}"'},
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

