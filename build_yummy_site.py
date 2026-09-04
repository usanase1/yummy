import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>YUMMY SNACKS - Homemade Goodness | Musanze Rwanda</title>
  <meta name="description" content="Artisan bakery in Musanze, Rwanda specializing in custom Wedding Cakes, Cakes, Breads, Mandazi, Sambusa & catering platters. Musanze - Inyuma ya Energy Radio. Order via 0792194867 / 0782464751.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-dark: #0A0806;
      --bg-card: #14110C;
      --bg-card-hover: #1E1A13;
      --gold-primary: #E9B949;
      --gold-light: #F7D785;
      --gold-dark: #B88E28;
      --terracotta-bg: #80341D;
      --text-main: #F4EFE6;
      --text-muted: #A69C8D;
      --border-gold: rgba(233, 185, 73, 0.25);
      --border-gold-strong: rgba(233, 185, 73, 0.6);
      --shadow-gold: 0 10px 30px rgba(233, 185, 73, 0.15);
      --radius-sm: 8px;
      --radius-md: 16px;
      --radius-lg: 24px;
      --font-heading: 'Cinzel', serif;
      --font-body: 'Plus Jakarta Sans', sans-serif;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      background-color: var(--bg-dark);
      color: var(--text-main);
      font-family: var(--font-body);
      line-height: 1.6;
      overflow-x: hidden;
    }

    /* Top Announcement Bar */
    .top-bar {
      background: #5E2412;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding: 8px 30px;
      font-size: 0.85rem;
      color: var(--gold-light);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .top-bar-contact a {
      color: var(--gold-primary);
      text-decoration: none;
      margin-left: 12px;
      font-weight: 600;
      transition: color 0.2s;
    }

    .top-bar-contact a:hover {
      color: #fff;
    }

    /* Navbar matching exact design from image */
    .navbar {
      position: sticky;
      top: 0;
      z-index: 1000;
      background-color: var(--terracotta-bg);
      border-bottom: 1px solid rgba(255, 255, 255, 0.15);
      padding: 18px 40px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }

    .nav-container {
      max-width: 1350px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .logo {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
    }

    .logo-emblem {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      border: 2px solid var(--gold-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle, #2A2010 0%, #0A0806 100%);
      box-shadow: 0 0 15px rgba(233, 185, 73, 0.3);
    }

    .logo-text-group {
      display: flex;
      flex-direction: column;
    }

    .logo-title {
      font-family: var(--font-heading);
      font-size: 1.25rem;
      font-weight: 800;
      color: #FFFFFF;
      letter-spacing: 1.5px;
      line-height: 1;
    }

    .logo-subtitle {
      font-size: 0.7rem;
      color: var(--gold-light);
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-top: 3px;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 40px;
      list-style: none;
    }

    .nav-links a {
      color: #FFFFFF;
      text-decoration: none;
      font-size: 1.05rem;
      font-weight: 300;
      letter-spacing: 2.5px;
      position: relative;
      padding-bottom: 6px;
      transition: all 0.3s ease;
      font-family: var(--font-body);
    }

    .nav-links a.active,
    .nav-links a:hover {
      color: #FFFFFF;
    }

    .nav-links a::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 0%;
      height: 2px;
      background-color: #FFFFFF;
      transition: width 0.3s ease;
    }

    .nav-links a.active::after,
    .nav-links a:hover::after {
      width: 100%;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .btn {
      padding: 10px 22px;
      border-radius: 30px;
      font-size: 0.9rem;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      transition: all 0.3s ease;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      border: none;
    }

    .btn-gold {
      background: linear-gradient(135deg, var(--gold-primary) 0%, var(--gold-dark) 100%);
      color: #0A0806;
      box-shadow: 0 4px 15px rgba(233, 185, 73, 0.3);
    }

    .btn-gold:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(233, 185, 73, 0.5);
      background: linear-gradient(135deg, var(--gold-light) 0%, var(--gold-primary) 100%);
    }

    .btn-outline {
      background: transparent;
      color: #FFFFFF;
      border: 1px solid rgba(255, 255, 255, 0.6);
    }

    .btn-outline:hover {
      background: rgba(255, 255, 255, 0.15);
      color: #fff;
      border-color: #FFFFFF;
    }

    .cart-btn {
      position: relative;
      background: rgba(0, 0, 0, 0.25);
      border: 1px solid rgba(255, 255, 255, 0.3);
      color: #FFFFFF;
      padding: 10px 18px;
      border-radius: 30px;
      cursor: pointer;
      font-size: 0.9rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: background 0.2s;
    }

    .cart-btn:hover {
      background: rgba(0, 0, 0, 0.4);
    }

    .cart-badge {
      background: var(--gold-primary);
      color: #0A0806;
      font-weight: 800;
      font-size: 0.75rem;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    /* Hero Section */
    .hero {
      position: relative;
      min-height: 85vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 80px 40px;
      background: linear-gradient(180deg, rgba(10, 8, 6, 0.4) 0%, var(--bg-dark) 100%),
                  url('assets/hero_wedding_cake_1788261874377.png') center/cover no-repeat;
    }

    .hero-overlay {
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at center, rgba(10,8,6,0.5) 0%, rgba(10,8,6,0.95) 100%);
    }

    .hero-content {
      position: relative;
      z-index: 2;
      max-width: 900px;
      text-align: center;
    }

    .hero-badge-group {
      display: flex;
      justify-content: center;
      gap: 16px;
      margin-bottom: 24px;
      flex-wrap: wrap;
    }

    .hero-badge {
      background: rgba(233, 185, 73, 0.1);
      border: 1px solid var(--border-gold);
      color: var(--gold-light);
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 600;
      letter-spacing: 1px;
      text-transform: uppercase;
    }

    .hero-title {
      font-family: var(--font-heading);
      font-size: clamp(2.5rem, 5vw, 4.5rem);
      font-weight: 900;
      color: #FFF;
      line-height: 1.15;
      margin-bottom: 20px;
      text-shadow: 0 4px 20px rgba(0,0,0,0.8);
    }

    .hero-title span {
      background: linear-gradient(135deg, var(--gold-light) 0%, var(--gold-primary) 50%, var(--gold-dark) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-desc {
      font-size: 1.15rem;
      color: var(--text-main);
      max-width: 650px;
      margin: 0 auto 36px;
      opacity: 0.9;
    }

    .hero-cta {
      display: flex;
      justify-content: center;
      gap: 20px;
      flex-wrap: wrap;
    }

    /* Section Styling */
    .section {
      padding: 100px 40px;
      max-width: 1300px;
      margin: 0 auto;
    }

    .section-header {
      text-align: center;
      margin-bottom: 60px;
    }

    .section-subtitle {
      color: var(--gold-primary);
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 3px;
      text-transform: uppercase;
      margin-bottom: 10px;
      display: block;
    }

    .section-title {
      font-family: var(--font-heading);
      font-size: clamp(2rem, 3.5vw, 3rem);
      color: #fff;
    }

    /* Circular Categories Bar */
    .category-showcase {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 24px;
      margin-bottom: 60px;
    }

    .cat-card {
      background: var(--bg-card);
      border: 1px solid var(--border-gold);
      border-radius: var(--radius-md);
      padding: 24px 16px;
      text-align: center;
      cursor: pointer;
      transition: all 0.3s ease;
      text-decoration: none;
    }

    .cat-card:hover {
      transform: translateY(-8px);
      border-color: var(--gold-primary);
      box-shadow: var(--shadow-gold);
      background: var(--bg-card-hover);
    }

    .cat-img-wrapper {
      width: 110px;
      height: 110px;
      border-radius: 50%;
      margin: 0 auto 16px;
      border: 2px solid var(--gold-primary);
      overflow: hidden;
      box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }

    .cat-img-wrapper img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }

    .cat-card:hover .cat-img-wrapper img {
      transform: scale(1.1);
    }

    .cat-name {
      font-family: var(--font-heading);
      font-size: 1.05rem;
      color: var(--gold-light);
      font-weight: 700;
    }

    /* Filter Tabs */
    .filter-tabs {
      display: flex;
      justify-content: center;
      gap: 12px;
      margin-bottom: 40px;
      flex-wrap: wrap;
    }

    .tab-btn {
      background: var(--bg-card);
      border: 1px solid var(--border-gold);
      color: var(--text-main);
      padding: 10px 24px;
      border-radius: 30px;
      cursor: pointer;
      font-size: 0.9rem;
      font-weight: 600;
      transition: all 0.2s;
    }

    .tab-btn.active, .tab-btn:hover {
      background: var(--gold-primary);
      color: #0A0806;
      border-color: var(--gold-primary);
    }

    /* Product Grid */
    .product-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 32px;
    }

    .product-card {
      background: var(--bg-card);
      border: 1px solid var(--border-gold);
      border-radius: var(--radius-md);
      overflow: hidden;
      transition: all 0.3s ease;
      display: flex;
      flex-direction: column;
    }

    .product-card:hover {
      transform: translateY(-6px);
      border-color: var(--gold-primary);
      box-shadow: var(--shadow-gold);
    }

    .product-img {
      height: 220px;
      width: 100%;
      object-fit: cover;
    }

    .product-body {
      padding: 24px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }

    .product-tag {
      font-size: 0.75rem;
      color: var(--gold-primary);
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 8px;
    }

    .product-title {
      font-family: var(--font-heading);
      font-size: 1.25rem;
      color: #fff;
      margin-bottom: 8px;
    }

    .product-desc {
      font-size: 0.9rem;
      color: var(--text-muted);
      margin-bottom: 20px;
      flex-grow: 1;
    }

    .product-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 16px;
      border-top: 1px solid rgba(255,255,255,0.08);
    }

    .product-price {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--gold-light);
    }

    /* Cake Customizer Section */
    .customizer-box {
      background: var(--bg-card);
      border: 1px solid var(--border-gold-strong);
      border-radius: var(--radius-lg);
      padding: 48px;
      box-shadow: 0 20px 50px rgba(0,0,0,0.6);
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 48px;
      align-items: center;
    }

    .customizer-preview {
      text-align: center;
    }

    .customizer-preview img {
      width: 100%;
      max-height: 380px;
      object-fit: cover;
      border-radius: var(--radius-md);
      border: 2px solid var(--gold-primary);
      box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    }

    .form-group {
      margin-bottom: 20px;
    }

    .form-label {
      display: block;
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--gold-light);
      margin-bottom: 8px;
    }

    .form-select, .form-input {
      width: 100%;
      padding: 12px 16px;
      background: #0A0806;
      border: 1px solid var(--border-gold);
      border-radius: var(--radius-sm);
      color: #fff;
      font-family: inherit;
      font-size: 0.95rem;
    }

    .form-select:focus, .form-input:focus {
      outline: none;
      border-color: var(--gold-primary);
    }

    .price-estimate {
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--gold-primary);
      margin: 20px 0;
      padding: 16px;
      background: rgba(233, 185, 73, 0.08);
      border-radius: var(--radius-sm);
      text-align: center;
      border: 1px dashed var(--border-gold);
    }

    /* Craftsmanship Section */
    .story-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 60px;
      align-items: center;
    }

    .story-img-container img {
      width: 100%;
      border-radius: var(--radius-lg);
      border: 2px solid var(--border-gold);
      box-shadow: 0 20px 40px rgba(0,0,0,0.7);
    }

    .story-text p {
      margin-bottom: 20px;
      color: var(--text-muted);
      font-size: 1.05rem;
    }

    .story-highlights {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-top: 30px;
    }

    .highlight-item {
      background: var(--bg-card);
      border: 1px solid var(--border-gold);
      padding: 16px;
      border-radius: var(--radius-sm);

    }

    .highlight-item h4 {
      color: var(--gold-primary);
      margin-bottom: 4px;
    }

    /* Location & Contact Section */
    .contact-banner {
      background: linear-gradient(135deg, #1C170E 0%, #0A0806 100%);
      border: 1px solid var(--border-gold-strong);
      border-radius: var(--radius-lg);
      padding: 50px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 40px;
    }

    .contact-info-list {
      list-style: none;
      margin-top: 24px;
    }

    .contact-info-list li {
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 1.05rem;
    }

    .contact-icon {
      color: var(--gold-primary);
      font-size: 1.3rem;
    }

    /* Footer */
    footer {
      background: #050403;
      border-top: 1px solid var(--border-gold);
      padding: 60px 40px 30px;
      text-align: center;
    }

    .footer-content {
      max-width: 1200px;
      margin: 0 auto 40px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 40px;
      text-align: left;
    }

    .footer-col h4 {
      font-family: var(--font-heading);
      color: var(--gold-primary);
      margin-bottom: 20px;
      font-size: 1.1rem;
    }

    .footer-col ul {
      list-style: none;
    }

    .footer-col ul li {
      margin-bottom: 10px;
    }

    .footer-col ul li a {
      color: var(--text-muted);
      text-decoration: none;
      transition: color 0.2s;
    }

    .footer-col ul li a:hover {
      color: var(--gold-primary);
    }

    .copyright {
      border-top: 1px solid rgba(255,255,255,0.05);
      padding-top: 24px;
      color: var(--text-muted);
      font-size: 0.85rem;
    }

    /* Order Drawer Modal */
    .drawer-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.8);
      z-index: 2000;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }

    .drawer-overlay.open {
      opacity: 1;
      pointer-events: auto;
    }

    .drawer {
      position: fixed;
      top: 0;
      right: -450px;
      width: 100%;
      max-width: 450px;
      height: 100vh;
      background: var(--bg-card);
      border-left: 1px solid var(--border-gold);
      z-index: 2001;
      transition: right 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      padding: 32px;
    }

    .drawer-overlay.open .drawer {
      right: 0;
    }

    .drawer-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-gold);
    }

    .drawer-title {
      font-family: var(--font-heading);
      color: var(--gold-primary);
      font-size: 1.3rem;
    }

    .close-drawer {
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 1.5rem;
      cursor: pointer;
    }

    .cart-items {
      flex-grow: 1;
      overflow-y: auto;
      margin-bottom: 20px;
    }

    .cart-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 12px 0;
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }

    .cart-item-name {
      font-weight: 600;
    }

    .cart-item-price {
      color: var(--gold-light);
    }

    @media (max-width: 900px) {
      .navbar {
        padding: 16px 20px;
      }
      .nav-links {
        gap: 20px;
      }
      .nav-links a {
        font-size: 0.9rem;
        letter-spacing: 1.5px;
      }
      .customizer-box, .story-grid, .contact-banner {
        grid-template-columns: 1fr;
      }
      .section {
        padding: 60px 20px;
      }
    }
  </style>
</head>
<body>

  <!-- Top Announcement Bar -->
  <div class="top-bar">
    <div>📍 <strong>Musanze</strong> — Inyuma ya Energy Radio | Fresh Baked Daily</div>
    <div class="top-bar-contact">
      <span>📞 Call Us:</span>
      <a href="tel:0792194867">0792194867</a>
      <a href="tel:0782464751">0782464751</a>
    </div>
  </div>

  <!-- Navbar matching user reference -->
  <nav class="navbar">
    <div class="nav-container">
      <a href="#" class="logo">
        <div class="logo-emblem">💛</div>
        <div class="logo-text-group">
          <span class="logo-title">YUMMY SNACKS</span>
          <span class="logo-subtitle">Homemade Goodness</span>
        </div>
      </a>

      <ul class="nav-links">
        <li><a href="#home" class="active">Home</a></li>
        <li><a href="#menu">Products</a></li>
        <li><a href="#story">Our Story</a></li>
        <li><a href="#categories">Inspire Me</a></li>
        <li><a href="#customizer">Seasonal</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>

      <div class="nav-actions">
        <button class="cart-btn" onclick="toggleCart()">
          🛒 Order Bag
          <span class="cart-badge" id="cartCount">0</span>
        </button>
        <a href="https://wa.me/250792194867" target="_blank" class="btn btn-gold">WhatsApp Order</a>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <section class="hero" id="home">
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <div class="hero-badge-group">
        <span class="hero-badge">✨ Fresh Ingredients</span>
        <span class="hero-badge">❤️ Made with Love</span>
        <span class="hero-badge">🏆 Great Taste</span>
      </div>
      <h1 class="hero-title">SWEETNESS & ARTISAN GOODNESS, <span>BAKED IN MUSANZE</span></h1>
      <p class="hero-desc">From magnificent multi-tiered wedding cakes to golden mandazi, artisan breads, and crispy sambusa — handcrafted fresh every single day.</p>
      <div class="hero-cta">
        <a href="#menu" class="btn btn-gold">EXPLORE MENU & PRODUCTS</a>
        <a href="#customizer" class="btn btn-outline">WEDDING CAKE CONSULTATION</a>
      </div>
    </div>
  </section>

  <!-- Category Showcase Bar -->
  <section class="section" id="categories">
    <div class="section-header">
      <span class="section-subtitle">OUR SPECIALTIES</span>
      <h2 class="section-title">Fresh Baked Categories</h2>
    </div>

    <div class="category-showcase">
      <div class="cat-card" onclick="filterCategory('wedding')">
        <div class="cat-img-wrapper">
          <img src="assets/hero_wedding_cake_1788261874377.png" alt="Wedding Cakes">
        </div>
        <div class="cat-name">Wedding Cakes</div>
      </div>

      <div class="cat-card" onclick="filterCategory('cakes')">
        <div class="cat-img-wrapper">
          <img src="assets/chocolate_cake_1788261898140.png" alt="Celebration Cakes">
        </div>
        <div class="cat-name">Cakes</div>
      </div>

      <div class="cat-card" onclick="filterCategory('bread')">
        <div class="cat-img-wrapper">
          <img src="assets/artisan_bread_1788261922619.png" alt="Artisan Breads">
        </div>
        <div class="cat-name">Bread</div>
      </div>

      <div class="cat-card" onclick="filterCategory('mandazi')">
        <div class="cat-img-wrapper">
          <img src="assets/golden_mandazi_1788261945527.png" alt="Golden Mandazi">
        </div>
        <div class="cat-name">Mandazi</div>
      </div>

      <div class="cat-card" onclick="filterCategory('sambusa')">
        <div class="cat-img-wrapper">
          <img src="assets/crispy_sambusa_1788261967770.png" alt="Crispy Sambusa">
        </div>
        <div class="cat-name">Sambusa</div>
      </div>

      <div class="cat-card" onclick="filterCategory('platters')">
        <div class="cat-img-wrapper">
          <img src="assets/baker_craft_1788261990529.png" alt="Event Platters">
        </div>
        <div class="cat-name">Event Platters</div>
      </div>
    </div>
  </section>

  <!-- Filterable Product Grid -->
  <section class="section" id="menu">
    <div class="section-header">
      <span class="section-subtitle">OUR CUSTOMERS LOVE</span>
      <h2 class="section-title">Most Ordered This Month</h2>
    </div>

    <div class="filter-tabs">
      <button class="tab-btn active" onclick="filterCategory('all', this)">All Snacks & Cakes</button>
      <button class="tab-btn" onclick="filterCategory('wedding', this)">Wedding Cakes</button>
      <button class="tab-btn" onclick="filterCategory('cakes', this)">Celebration Cakes</button>
      <button class="tab-btn" onclick="filterCategory('bread', this)">Fresh Breads</button>
      <button class="tab-btn" onclick="filterCategory('mandazi', this)">Golden Mandazi</button>
      <button class="tab-btn" onclick="filterCategory('sambusa', this)">Sambusa & Snacks</button>
    </div>

    <div class="product-grid" id="productGrid">
      <!-- Product 1 -->
      <div class="product-card" data-category="wedding">
        <img src="assets/hero_wedding_cake_1788261874377.png" class="product-img" alt="Royal Wedding Cake">
        <div class="product-body">
          <span class="product-tag">Wedding Cake</span>
          <h3 class="product-title">Three-Tier Ivory & Gold Luxury Cake</h3>
          <p class="product-desc">Serves 80–120 guests. Custom sugar roses, gold leaf detailing, and your choice of vanilla & chocolate tiers.</p>
          <div class="product-footer">
            <span class="product-price">140,000 RWF</span>
            <button class="btn btn-gold" onclick="addToCart('Three-Tier Ivory & Gold Cake', 140000)">+ Order</button>
          </div>
        </div>
      </div>

      <!-- Product 2 -->
      <div class="product-card" data-category="cakes">
        <img src="assets/chocolate_cake_1788261898140.png" class="product-img" alt="Chocolate Fudge Cake">
        <div class="product-body">
          <span class="product-tag">Birthday / Celebration</span>
          <h3 class="product-title">Belgian Chocolate Fudge Ganache Cake</h3>
          <p class="product-desc">Rich cocoa layers with silky drip ganache frosting. 20cm round, 12 generous slices.</p>
          <div class="product-footer">
            <span class="product-price">22,000 RWF</span>
            <button class="btn btn-gold" onclick="addToCart('Chocolate Fudge Ganache Cake', 22000)">+ Order</button>
          </div>
        </div>
      </div>

      <!-- Product 3 -->
      <div class="product-card" data-category="bread">
        <img src="assets/artisan_bread_1788261922619.png" class="product-img" alt="Artisan Bread Loaves">
        <div class="product-body">
          <span class="product-tag">Fresh Bakery</span>
          <h3 class="product-title">Homestyle Honey Wheat Loaf (Pack of 2)</h3>
          <p class="product-desc">Golden crust, soft interior baked with pure honey and local butter. Perfect for breakfast.</p>
          <div class="product-footer">
            <span class="product-price">3,500 RWF</span>
            <button class="btn btn-gold" onclick="addToCart('Honey Wheat Loaf (Pack of 2)', 3500)">+ Order</button>
          </div>
        </div>
      </div>

      <!-- Product 4 -->
      <div class="product-card" data-category="mandazi">
        <img src="assets/golden_mandazi_1788261945527.png" class="product-img" alt="Golden Mandazi">
        <div class="product-body">
          <span class="product-tag">Snacks & Tea Time</span>
          <h3 class="product-title">Golden Cardamom Mandazi (Dozen of 12)</h3>
          <p class="product-desc">Lightly sweet, fluffy, fried fresh every morning with warm cardamom & coconut notes.</p>
          <div class="product-footer">
            <span class="product-price">3,000 RWF</span>
            <button class="btn btn-gold" onclick="addToCart('Cardamom Mandazi (Dozen)', 3000)">+ Order</button>
          </div>
        </div>
      </div>

      <!-- Product 5 -->
      <div class="product-card" data-category="sambusa">
        <img src="assets/crispy_sambusa_1788261967770.png" class="product-img" alt="Crispy Beef Sambusa">
        <div class="product-body">
          <span class="product-tag">Savory Snacks</span>
          <h3 class="product-title">Crispy Beef & Herb Sambusa (Pack of 10)</h3>
          <p class="product-desc">Thin crispy pastry filled with seasoned minced beef, scallions, and fragrant spices.</p>
          <div class="product-footer">
            <span class="product-price">5,000 RWF</span>
            <button class="btn btn-gold" onclick="addToCart('Crispy Beef Sambusa (Pack of 10)', 5000)">+ Order</button>
          </div>
        </div>
      </div>

      <!-- Product 6 -->
      <div class="product-card" data-category="platters">
        <img src="assets/baker_craft_1788261990529.png" class="product-img" alt="Event Snack Platter">
        <div class="product-body">
          <span class="product-tag">Catering & Events</span>
          <h3 class="product-title">Grand Musanze Snack & Pastry Platter</h3>
          <p class="product-desc">Feeds 20 guests. Includes 15 Mandazi, 15 Sambusa, mini cake bites, and savory pastries.</p>
          <div class="product-footer">
            <span class="product-price">35,000 RWF</span>
            <button class="btn btn-gold" onclick="addToCart('Grand Snack Platter (20 guests)', 35000)">+ Order</button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Interactive Wedding Cake Customizer -->
  <section class="section" id="customizer">
    <div class="section-header">
      <span class="section-subtitle">WEDDING CAKE CONSULTATION</span>
      <h2 class="section-title">Customize Your Dream Wedding Cake</h2>
    </div>

    <div class="customizer-box">
      <div class="customizer-preview">
        <img src="assets/hero_wedding_cake_1788261874377.png" alt="Custom Wedding Cake Preview">
        <p style="margin-top:12px; color:var(--text-muted); font-size:0.85rem;">* Handcrafted in Musanze with custom delivery to your venue.</p>
      </div>

      <div class="customizer-form">
        <div class="form-group">
          <label class="form-label">Number of Tiers</label>
          <select class="form-select" id="tierSelect" onchange="calculateCakePrice()">
            <option value="1">1-Tier Cake (Serves 20–30) — 45,000 RWF</option>
            <option value="2">2-Tier Cake (Serves 50–70) — 85,000 RWF</option>
            <option value="3" selected>3-Tier Cake (Serves 90–120) — 140,000 RWF</option>
            <option value="4">4-Tier Grand Cake (Serves 150–200) — 210,000 RWF</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label">Primary Cake Flavor</label>
          <select class="form-select" id="flavorSelect">
            <option>Vanilla Bean Buttercream</option>
            <option>Belgian Chocolate Ganache</option>
            <option>Red Velvet & Cream Cheese</option>
            <option>Passionfruit & Mango Twist</option>
            <option>Marble Chocolate Vanilla</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label">Design & Frosting Style</label>
          <select class="form-select" id="styleSelect">
            <option>Royal Gold Leaf & Roses</option>
            <option>Minimalist Semi-Naked Floral</option>
            <option>Classic White Fondant & Pearls</option>
            <option>Textured Gold Drip & Berries</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label">Wedding Date & Venue Location</label>
          <input type="text" class="form-input" id="weddingDetails" placeholder="e.g. Oct 15th, Fatima Hotel Musanze">
        </div>

        <div class="price-estimate" id="cakePriceDisplay">
          Estimated Price: 140,000 RWF
        </div>

        <button class="btn btn-gold" style="width: 100%; justify-content: center; padding: 14px;" onclick="sendWeddingQuote()">
          💬 Request WhatsApp Quote & Booking
        </button>
      </div>
    </div>
  </section>

  <!-- Craftsmanship / Our Story -->
  <section class="section" id="story">
    <div class="story-grid">
      <div class="story-text">
        <span class="section-subtitle">OUR CRAFTSMANSHIP</span>
        <h2 class="section-title" style="margin-bottom: 20px;">Baking in Musanze with Passion</h2>
        <p>At <strong>Yummy Snacks</strong>, we believe every celebration deserves the unmatched warmth of homemade baking. Located right in Musanze behind Energy Radio, our bakery blends traditional Rwandan hospitality with modern culinary art.</p>
        <p>Whether you're organizing a wedding at a local hotel, ordering daily breakfast mandazi for your family, or arranging catering platters for your company, we use only fresh, premium local ingredients.</p>

        <div class="story-highlights">
          <div class="highlight-item">
            <h4>📍 Musanze Location</h4>
            <p style="font-size:0.85rem; margin:0;">Inyuma ya Energy Radio</p>
          </div>
          <div class="highlight-item">
            <h4>⏰ Daily Baking</h4>
            <p style="font-size:0.85rem; margin:0;">Fresh every morning at 7 AM</p>
          </div>
        </div>
      </div>

      <div class="story-img-container">
        <img src="assets/baker_craft_1788261990529.png" alt="Yummy Snacks Bakery Craft">
      </div>
    </div>
  </section>

  <!-- Contact & Location Banner -->
  <section class="section" id="contact">
    <div class="contact-banner">
      <div>
        <span class="section-subtitle">VISIT OR CALL US</span>
        <h2 class="section-title" style="margin-bottom: 16px;">We're Ready for Your Order</h2>
        <p style="color: var(--text-muted);">Stop by our bakery in Musanze or place an instant order over WhatsApp for home or venue delivery.</p>

        <ul class="contact-info-list">
          <li><span class="contact-icon">📍</span> <strong>Address:</strong> Musanze — Inyuma ya Energy Radio</li>
          <li><span class="contact-icon">📞</span> <strong>Phone 1:</strong> <a href="tel:0792194867" style="color:var(--gold-primary);">0792194867</a></li>
          <li><span class="contact-icon">📞</span> <strong>Phone 2:</strong> <a href="tel:0782464751" style="color:var(--gold-primary);">0782464751</a></li>
          <li><span class="contact-icon">⏰</span> <strong>Hours:</strong> Mon–Sat: 7:00 AM – 8:00 PM | Sun: 9:00 AM – 5:00 PM</li>
        </ul>
      </div>

      <div style="display: flex; flex-direction: column; justify-content: center; gap: 20px;">
        <a href="https://wa.me/250792194867?text=Hello%20Yummy%20Snacks!%20I%20would%20like%20to%20place%20an%20order." target="_blank" class="btn btn-gold" style="padding: 16px; justify-content: center; font-size: 1.05rem;">
          💬 Chat on WhatsApp (0792194867)
        </a>
        <a href="tel:0782464751" class="btn btn-outline" style="padding: 16px; justify-content: center; font-size: 1.05rem;">
          📞 Direct Phone Call (0782464751)
        </a>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="footer-content">
      <div class="footer-col">
        <h4>YUMMY SNACKS</h4>
        <p style="color:var(--text-muted); font-size:0.9rem;">Homemade Goodness baked daily in Musanze. Specializing in custom Wedding Cakes, celebration pastries, fresh mandazi & sambusa.</p>
      </div>

      <div class="footer-col">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#menu">Product Menu</a></li>
          <li><a href="#customizer">Wedding Cake Builder</a></li>
          <li><a href="#story">Our Story</a></li>
          <li><a href="#contact">Contact Us</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Contact Musanze</h4>
        <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom: 8px;">Inyuma ya Energy Radio, Musanze, Northern Province, Rwanda</p>
        <p style="color:var(--gold-primary); font-weight:700;">0792194867 / 0782464751</p>
      </div>
    </div>

    <div class="copyright">
      &copy; 2026 YUMMY SNACKS - Homemade Goodness. All rights reserved. Musanze, Rwanda.
    </div>
  </footer>

  <!-- Slide-out Cart Drawer -->
  <div class="drawer-overlay" id="drawerOverlay" onclick="toggleCart()">
    <div class="drawer" onclick="event.stopPropagation()">
      <div class="drawer-header">
        <h3 class="drawer-title">Your Order Bag</h3>
        <button class="close-drawer" onclick="toggleCart()">&times;</button>
      </div>

      <div class="cart-items" id="cartItemsList">
        <p style="color: var(--text-muted); text-align: center; margin-top: 40px;">Your bag is currently empty.</p>
      </div>

      <div style="border-top: 1px solid var(--border-gold); padding-top: 16px;">
        <div style="display: flex; justify-content: space-between; font-size: 1.2rem; font-weight: 800; color: var(--gold-primary); margin-bottom: 16px;">
          <span>Total:</span>
          <span id="cartTotal">0 RWF</span>
        </div>
        <button class="btn btn-gold" style="width: 100%; justify-content: center; padding: 14px;" onclick="checkoutWhatsApp()">
          📲 Send Order via WhatsApp
        </button>
      </div>
    </div>
  </div>

  <!-- JavaScript Interaction -->
  <script>
    let cart = [];

    // Active nav link highlight on click
    document.querySelectorAll('.nav-links a').forEach(link => {
      link.addEventListener('click', function() {
        document.querySelectorAll('.nav-links a').forEach(l => l.classList.remove('active'));
        this.classList.add('active');
      });
    });

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

    function sendWeddingQuote() {
      const tier = document.getElementById('tierSelect').options[document.getElementById('tierSelect').selectedIndex].text;
      const flavor = document.getElementById('flavorSelect').value;
      const style = document.getElementById('styleSelect').value;
      const details = document.getElementById('weddingDetails').value || "Musanze venue";

      const text = `Hello Yummy Snacks! I would like a quote for a Wedding Cake:%0A- Tiers: ${tier}%0A- Flavor: ${flavor}%0A- Style: ${style}%0A- Date/Venue: ${details}`;
      window.open(`https://wa.me/250792194867?text=${text}`, '_blank');
    }

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
            <button style="background:none; border:none; color:red; cursor:pointer;" onclick="removeFromCart(${index})">&times;</button>
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
  </script>
</body>
</html>
"""

# Write to both files
with open(r'c:\Users\emeli\Downloads\Yummy\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open(r'c:\Users\emeli\Downloads\Yummy\Yummy Snacks Website.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Successfully updated index.html and Yummy Snacks Website.html with exact terracotta navbar design.")
