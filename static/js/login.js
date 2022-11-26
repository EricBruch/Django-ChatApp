const login = async () => {
  prepare();
  const res = await sendLogin();

  if (res.ok) {
    onSuccess(res);
  } else {
    onWsError();
  }
};

const prepare = () => {
  invalidCredentials.innerHTML = "";
  someError.innerHTML = "";
  fieldset.disabled = true;
  loginBtn.disabled = true;
  loadingSpinner.classList.remove("hidden");
};

const sendLogin = async () => {
  const fd = new FormData();
  fd.append("username", username.value);
  fd.append("password", password.value);
  fd.append("csrfmiddlewaretoken", getCsrfToken());

  const res = await callPostEndpoint(fd, "/login/");
  loadingSpinner.classList.add("hidden");
  fieldset.disabled = false;
  loginBtn.disabled = false;
  return res;
};

const onSuccess = async (response) => {
  const json = JSON.parse(await response.json());
  if (json.invalid) {
    invalidCredentials.innerHTML += `
      <p class="color-red">Credentials entered are invalid</p>
      `;
  } else {
    location.href = '/chat/';
  }
};

const onWsError = () => {
  someError.innerHTML += `<p class="color-red">Some Error occured</p>`;
};
