from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import numpy as np
from sklearn.linear_model import LinearRegression
import uvicorn

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="supersecret")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    # Берём старые значения из сессии, если есть
    x = request.session.get("x_values", [])
    y = request.session.get("y_values", [])
    return templates.TemplateResponse("index.html", {"request": request, "x": x, "y": y})

@app.post("/", response_class=HTMLResponse)
def predict(request: Request,
            x_values: str = Form(...),
            y_values: str = Form(...)):

    try:
        x = np.array([float(i) for i in x_values.split(",")]).reshape(-1, 1)
        y = np.array([float(i) for i in y_values.split(",")])

        if len(x) != len(y):
            return templates.TemplateResponse(
                "index.html",
                {"request": request, "error": "Количество X и Y должно совпадать!"}
            )

        model = LinearRegression()
        model.fit(x, y)

        next_x = float(max(x_values.split(","), key=float)) + 1
        next_y = model.predict([[next_x]])[0]

        x_plot = list(x.flatten()) + [next_x]
        y_plot = list(y) + [round(next_y, 2)]

        # Сохраняем значения в сессии, чтобы они оставались после POST
        request.session["x_values"] = x_plot
        request.session["y_values"] = y_plot

        return templates.TemplateResponse(
            "index.html",
            {"request": request, "x": x_plot, "y": y_plot}
        )

    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": f"Ошибка: {e}"}
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
