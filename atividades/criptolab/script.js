// Utilidades
const alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const mod = (n, m) => (n % m + m) % m;

// Tabs
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.onclick = () => {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(btn.dataset.tab).classList.add('active');
  };
});

// === CÉSAR ===
function cesar(texto, k, modo = 1) {
  return texto.toUpperCase().split('').map(c => {
    if (alpha.includes(c)) {
      const i = alpha.indexOf(c);
      return alpha[mod(i + modo * k, 26)];
    }
    return c;
  }).join('');
}

function criptografarCesar() {
  const k = parseInt(document.getElementById('cesar-k').value);
  const plain = document.getElementById('cesar-plain').value;
  document.getElementById('cesar-crypto').textContent = cesar(plain, k);
}

function forcaBrutaCesar() {
  const crypto = "FRQILGHQFLDO";
  let result = "";
  for (let k = 0; k < 26; k++) {
    const dec = cesar(crypto, k, -1);
    if (dec.includes("CONFIDENCIAL")) {
      result = `<strong>k=${k} → ${dec}</strong>`;
      break;
    }
    result += `k=${k}: ${dec}<br>`;
  }
  document.getElementById('cesar-brute').innerHTML = result;
}

// === VIGENÈRE ===
function vigenere(texto, chave, modo = 1) {
  chave = chave.toUpperCase().replace(/[^A-Z]/g, '');
  texto = texto.toUpperCase();
  let result = "", j = 0;
  for (let c of texto) {
    if (alpha.includes(c)) {
      const k = alpha.indexOf(chave[j % chave.length]);
      result += alpha[mod(alpha.indexOf(c) + modo * k, 26)];
      j++;
    } else {
      result += c;
    }
  }
  return result;
}

function criptografarVigenere() {
  const key = document.getElementById('vig-key').value;
  const plain = document.getElementById('vig-plain').value;
  document.getElementById('vig-crypto').textContent = vigenere(plain, key);
}

function descriptografarVigenere() {
  document.getElementById('vig-decrypto').textContent = vigenere("WEVIFQILG", "CHAVE", -1);
}

// === ENIGMA (simulação simples) ===
function enigmaSim(texto) {
  // Simulação mínima com 3 rotores fixos
  const rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ";
  const rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE";
  const rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO";
  let out = "";
  for (let i = 0; i < texto.length; i++) {
    let c = texto[i];
    if (!alpha.includes(c)) { out += c; continue; }
    let idx = alpha.indexOf(c);
    idx = rotor3[idx];
    idx = alpha.indexOf(rotor2[alpha.indexOf(idx)]);
    idx = alpha.indexOf(rotor1[idx]);
    out += idx;
  }
  return out;
}

function criptografarEnigma() {
  const plain = document.getElementById('enigma-plain').value.toUpperCase();
  document.getElementById('enigma-crypto').textContent = enigmaSim(plain);
}

// === RSA ===
function modPow(base, exp, mod) {
  let result = 1;
  base = base % mod;
  while (exp > 0) {
    if (exp % 2 === 1) result = (result * base) % mod;
    exp = Math.floor(exp / 2);
    base = (base * base) % mod;
  }
  return result;
}

function criptografarRSA() {
  const msg = [18,4,6,20,11,0];
  const e = 17, n = 3233;
  const crypto = msg.map(m => modPow(m, e, n));
  document.getElementById('rsa-crypto').textContent = `[${crypto.join(', ')}]`;
}

function descriptografarRSA() {
  const crypto = [2870,179,1021,1,2153,179];
  const d = 2753, n = 3233;
  const plain = crypto.map(c => modPow(c, d, n));
  const letras = plain.map(n => alpha[n] || '?').join(' ');
  document.getElementById('rsa-decrypto').textContent = `${plain} → ${letras}`;
}

// === HASH ===
async function sha256(text) {
  const encoder = new TextEncoder();
  const data = encoder.encode(text);
  const hash = await crypto.subtle.digest('SHA-256', data);
  return Array.from(new Uint8Array(hash)).map(b => b.toString(16).padStart(2, '0')).join('');
}

async function calcularHash() {
  const t1 = document.getElementById('hash1').value;
  const t2 = document.getElementById('hash2').value;
  const h1 = await sha256(t1);
  const h2 = await sha256(t2);
  document.getElementById('h1').textContent = h1;
  document.getElementById('h2').textContent = h2;

  let diff = 0;
  for (let i = 0; i < h1.length; i++) if (h1[i] !== h2[i]) diff++;
  document.getElementById('diff').textContent = diff * 4 + " bits";
}

async function hashArquivo() {
  const file = document.getElementById('file-input').files[0];
  if (!file) return alert("Selecione um arquivo");
  const arrayBuffer = await file.arrayBuffer();
  const hash = await crypto.subtle.digest('SHA-256', arrayBuffer);
  const hex = Array.from(new Uint8Array(hash)).map(b => b.toString(16).padStart(2, '0')).join('');
  document.getElementById('file-hash').textContent = hex;
}