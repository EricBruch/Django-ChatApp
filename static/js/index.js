const saveMessage = async () => {
  prepare();
  const response = await loadMessage();

  if (response.ok) {
    success(response);
  } else {
    errorHandling();
  }
};

const prepare = () => {
  loadingSpinner.classList.remove("hidden");
  preliminaryAddText(getDateString(new Date()), messageField.value);
}

const preliminaryAddText = (date, text) => {
  messageContainer.innerHTML += `
    <div id="deleteMessage">
      <span class="color-gray">[${date}]:</span>
      ${getUser()}: <i class="color-gray">${text}</i>
    </div>
    `;
};

const loadMessage = async () => {
  const fd = new FormData();
  fd.append("message", messageField.value);
  fd.append("csrfmiddlewaretoken", getCsrfToken());

  const res = await fetch("/chat/", {
    method: "POST",
    body: fd,
  });
  loadingSpinner.classList.add("hidden");
  return res;
};

const errorHandling = () => {
  messageContainer.innerHTML += `<div class="color-red">An Error occured sending above message</div>`;
};

const success = async (response) => {
  deleteMessage.remove();
  const json = JSON.parse(await response.json());
  addText(
    getDateString(new Date(`${json.fields.created_at}`)),
    json.fields.text
  );
};

const addText = (date, text) => {
  messageContainer.innerHTML += `
    <div>
      <span class="color-gray">[${date}]:</span>
      ${getUser()}: <i>${text}</i>
    </div>
    `;
};

const getDateString = (date) => {
  const month = date.toLocaleDateString("en-US", { month: "short" });
  const day = date.toLocaleDateString("en-US", { day: "numeric" });
  const year = date.toLocaleDateString("en-US", { year: "numeric" });

  return `${month}. ${day}, ${year}`;
};
