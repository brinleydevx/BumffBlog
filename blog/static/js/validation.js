// Lightweight client-side validation for username and password
function scorePassword(pw) {
  if (!pw) return 0;
  let score = 0;
  if (pw.length >= 8) score += 1;
  if (pw.length >= 12) score += 1;
  if (/[a-z]/.test(pw)) score += 1;
  if (/[A-Z]/.test(pw)) score += 1;
  if (/[0-9]/.test(pw)) score += 1;
  if (/[^A-Za-z0-9]/.test(pw)) score += 1;
  return score; // 0-6
}

function strengthText(score) {
  if (score <= 1) return {text: 'Very weak', color: '#ef4444'};
  if (score <= 2) return {text: 'Weak', color: '#f59e0b'};
  if (score <= 3) return {text: 'Fair', color: '#f59e0b'};
  if (score <= 4) return {text: 'Good', color: '#10b981'};
  return {text: 'Strong', color: '#059669'};
}

function validateUsernameNoSpaces(value) {
  if (!value) return {ok: false, msg: 'Username required'};
  if (/\s/.test(value)) return {ok: false, msg: 'Username cannot contain spaces'};
  if (value.length < 3) return {ok: false, msg: 'Minimum 3 characters'};
  return {ok: true, msg: 'Looks good'};
}

function initValidation() {
  const username = document.getElementById('username') || document.querySelector('input[name="username"]');
  const unameFb = document.getElementById('username-feedback');
  if (username && unameFb) {
    username.addEventListener('input', function(){
      const res = validateUsernameNoSpaces(this.value.trim());
      unameFb.textContent = res.msg;
      unameFb.style.color = res.ok ? '#10b981' : '#ef4444';
    });
  }

  const password = document.getElementById('password') || document.querySelector('input[name="password"]');
  const pwBar = document.getElementById('password-strength-fill');
  const pwText = document.getElementById('password-feedback');
  if (password && pwBar && pwText) {
    password.addEventListener('input', function(){
      const s = scorePassword(this.value);
      const pct = Math.round((s / 6) * 100);
      pwBar.style.width = pct + '%';
      const st = strengthText(s);
      pwBar.style.background = st.color;
      pwText.textContent = st.text;
      pwText.style.color = st.color;
    });
  }
}

// expose for inline init
window.initValidation = initValidation;
