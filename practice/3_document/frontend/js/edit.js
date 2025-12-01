// Получаем имя файла из URL
const params = new URLSearchParams(window.location.search);
const file = params.get("file");
document.getElementById("filename").textContent = `Файл: ${file}`;

const textarea = document.getElementById("fileContent");

// Загружаем содержимое файла с сервера
async function loadFile() {
    const response = await fetch(`http://localhost:8000/files/${encodeURIComponent(file)}`);
    const data = await response.json(); // { content: "текст файла" }
    textarea.value = data.content;
}

loadFile();

// Сохраняем изменения
document.getElementById("saveBtn").onclick = async () => {
    const newContent = textarea.value;

    const response = await fetch(`http://localhost:8000/files/${encodeURIComponent(file)}`, {
        method: "POST", // или PUT
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content: newContent })
    });

    const result = await response.json();
    alert(result.status); // например "успешно сохранено"
};