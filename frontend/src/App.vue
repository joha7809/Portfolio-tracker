<template>
  <div class="app-layout">
    <header>
      <nav>
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/welcome">Welcome</router-link></li>
          <li><router-link to="/profile">Profile</router-link></li>
          <li><a href="/accounts/login">Login</a></li>
        </ul>
      </nav>
    </header>

    <main>
      <router-view />
    </main>
  </div>
</template>

<style scoped>
/* Define the custom property at the root level */
:root {
  --main-bg-color: #ffae007a;
  /* Define the background color variable */
}

.app-layout {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

header {
  background: #f8f9fa;
  border-bottom: 1px solid #ddd;
  padding: 1rem 2rem;
}

li {}

nav ul {
  display: flex;
  gap: 2rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

nav a {
  color: #42b983;
  text-decoration: none;
  font-size: 1.1rem;
  font-weight: 500;
}

nav a.router-link-exact-active {
  color: #2c3e50;
  font-weight: bold;
}

main {
  flex: 1;
  padding: 2rem;
  width: 100%;
  margin: 0 auto;
  background-color: var(--main-bg-color);
  /* Use the custom property */
}
</style>
