const register = async () => {
  reset();

  if (!preChecks()) return;

  prepare();
  const res = await sendLogin();

  if (res.ok) {
    onSuccess(res);
  } else {
    onWsError();
  }
};

const reset = () => {};

const prepare = () => {
  loadingSpinner.classList.remove("hidden");
  fieldset.disabled = true;
  registerBtn.disabled = true;
};

const preChecks = () => {
  const [nameVal, emailVal, pVal, pRepVal] = [
    username.value,
    email.value,
    password.value,
    passwordRepeat.value,
  ];
  if (!nameVal || !emailVal || !pVal || !pRepVal) {
    displayInvald();
    return false;
  }
  if (pVal !== pRepVal) {
    pwNotMatching();
    return false;
  }
  return true;
};

const pwNotMatching = () => {
  notMatching.innerHTML += `<p class="color-red">Password not matching</p>`;
};

const displayInvald = () => {
  provideValidInput.innerHTML += `<p class="color-red">Provide valid data</p>`;
};

const sendLogin = async () => {
  const fd = new FormData();
  fd.append("username", username.value);
  fd.append("email", email.value);
  fd.append("password", password.value);
  fd.append("passwordRepeat", passwordRepeat.value);
  fd.append("csrfmiddlewaretoken", getCsrfToken());

  const res = await callPostEndpoint(fd, "/register/");
  loadingSpinner.classList.add("hidden");
  fieldset.disabled = false;
  registerBtn.disabled = false;
  return res;
};

const onSuccess = async (response) => {
  const json = JSON.parse(await response.json());
  if (json.successful) {
    location.href = "/chat/";
    return;
  }
  if (json.notMatching) {
    pwNotMatching();
  }
};

const onWsError = () => {
  someError.innerHTML += `<p class="color-red">Some Error occured</p>`;
};
