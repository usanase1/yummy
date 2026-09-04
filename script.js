/* ==========================================================================
   YUMMY SNACKS - Pure JavaScript Logic (Theme Switcher, Cart & Customizer)
   ========================================================================== */

let cart = [];

// Initialize Theme Mode on Load
document.addEventListener('DOMContentLoaded', () => {
  const savedTheme = localStorage.getItem('yummyTheme') || 'dark';
  setTheme(savedTheme);

  // Active nav link highlight on scroll/click
  const links = document.querySelectorAll('.nav-links a');
  links.forEach(link => {
    link.addEventListener('click', function() {
      links.forEach(l => l.classList.remove('active'));
      this.classList.add('active');
    });
  });
});

// Toggle Dark & Light Mode
function toggleTheme() {
  const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  setTheme(newTheme);
}

function setTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('yummyTheme', theme);
  
  const icon = document.getElementById('themeIcon');
  const text = document.getElementById('themeText');
  if (theme === 'light') {
    if (icon) icon.innerText = '🌙';
    if (text) text.innerText = 'Dark Mode';
  } else {
    if (icon) icon.innerText = '☀️';
    if (text) text.innerText = 'Light Mode';
  }
}

// Filter Product Grid
function filterCategory(category, element) {
  if (element) {
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    element.classList.add('active');
  }

  const cards = document.querySelectorAll('.product-card');
  cards.forEach(card => {
    if (category === 'all' || card.dataset.category === category) {
      card.style.display = 'flex';
    } else {
      card.style.display = 'none';
    }
  });
}

// Wedding Cake Price Calculator
function calculateCakePrice() {
  const select = document.getElementById('tierSelect');
  const val = select.value;
  let price = "140,000 RWF";
  if (val === "1") price = "45,000 RWF";
  if (val === "2") price = "85,000 RWF";
  if (val === "3") price = "140,000 RWF";
  if (val === "4") price = "210,000 RWF";

  document.getElementById('cakePriceDisplay').innerText = `Estimated Price: ${price}`;
}

// Request Wedding Cake WhatsApp Quote
function sendWeddingQuote() {
  const tier = document.getElementById('tierSelect').options[document.getElementById('tierSelect').selectedIndex].text;
  const flavor = document.getElementById('flavorSelect').value;
  const style = document.getElementById('styleSelect').value;
  const details = document.getElementById('weddingDetails').value || "Musanze venue";

  const text = `Hello Yummy Snacks! I would like a quote for a Wedding Cake:%0A- Tiers: ${tier}%0A- Flavor: ${flavor}%0A- Style: ${style}%0A- Date/Venue: ${details}`;
  window.open(`https://wa.me/250792194867?text=${text}`, '_blank');
}

// Shopping Bag Functions
function addToCart(name, price) {
  cart.push({ name, price });
  updateCartUI();
  toggleCart(true);
}

function updateCartUI() {
  document.getElementById('cartCount').innerText = cart.length;
  const list = document.getElementById('cartItemsList');
  if (cart.length === 0) {
    list.innerHTML = '<p style="color: var(--text-muted); text-align: center; margin-top: 40px;">Your bag is currently empty.</p>';
    document.getElementById('cartTotal').innerText = '0 RWF';
    return;
  }

  let total = 0;
  let html = '';
  cart.forEach((item, index) => {
    total += item.price;
    html += `
      <div class="cart-item">
        <div>
          <div class="cart-item-name">${item.name}</div>
          <div class="cart-item-price">${item.price.toLocaleString()} RWF</div>
        </div>
        <button style="background:none; border:none; color:red; cursor:pointer; font-size:1.2rem;" onclick="removeFromCart(${index})">&times;</button>
      </div>
    `;
  });

  list.innerHTML = html;
  document.getElementById('cartTotal').innerText = `${total.toLocaleString()} RWF`;
}

function removeFromCart(index) {
  cart.splice(index, 1);
  updateCartUI();
}

function toggleCart(forceOpen) {
  const overlay = document.getElementById('drawerOverlay');
  if (forceOpen) {
    overlay.classList.add('open');
  } else {
    overlay.classList.toggle('open');
  }
}

function checkoutWhatsApp() {
  if (cart.length === 0) {
    alert("Your bag is empty!");
    return;
  }

  let itemsText = cart.map(i => `- ${i.name} (${i.price.toLocaleString()} RWF)`).join('%0A');
  let total = cart.reduce((sum, i) => sum + i.price, 0);
  let text = `Hello Yummy Snacks! I would like to place an order:%0A${itemsText}%0A%0A*Total: ${total.toLocaleString()} RWF*%0APlease confirm availability and delivery to Musanze.`;

  window.open(`https://wa.me/250792194867?text=${text}`, '_blank');
}
