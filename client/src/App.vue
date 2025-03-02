<script setup lang="ts">
import { onMounted } from 'vue';
import WebSocketClient from './client'

onMounted(async () => {
  const url = "https://echo.websocket.org/"

  const client = new WebSocketClient(url);

  client.onConnect(() => {
    console.log('Connected to server');
  });
  client.onMessageReceived((message) => {
    console.log('Message received:', message);
  });

  await client.connect();
  client.sendMessage('Hello');
});
</script>

<template>
  <h1>Hello</h1>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
