document.getElementById("loadBtn").onclick = async () => {
    // Получаем JSON с сервера
    const response = await fetch("http://localhost:8000/files");
    const data = await response.json();

    const fileList = document.getElementById("fileList");
    fileList.innerHTML = ""; // очищаем список перед добавлением

    data.files.forEach(file => {
        const li = document.createElement("li");

        // Название файла
        const span = document.createElement("span");
        span.textContent = file;

        // Кнопка "Изменить"
        const button = document.createElement("button");
        button.textContent = "Изменить";
        button.onclick = () => {
        window.location.href = `edit.html?file=${encodeURIComponent(file)}`;
    };

        li.appendChild(span);
        li.appendChild(button);
        fileList.appendChild(li);
    });
};
