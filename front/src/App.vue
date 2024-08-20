<template>
  <div id="app" class="container mt-5">
    <div class="mb-3">
      <input v-model="inputUrl" type="text" class="form-control" placeholder="Enter URL" />
      <button @click="submitUrl" class="btn btn-primary mt-2">Submit</button>
    </div>
    <!-- Conditionally render UrlTable component -->
    <UrlTable v-if="showUrlTable" :urls="urls" />
  </div>
</template>

<script>
import UrlTable from './components/UrlTable.vue';
import axios from 'axios';

export default {
  name: 'App',
  components: {
    UrlTable,
  },
  data() {
    return {
      inputUrl: '',
      urls: [],
      showUrlTable: false,
    };
  },
  methods: {
    async submitUrl() {
      if (!this.inputUrl) {
        alert('Please enter a URL.');
        return;
      }
      try {
        const response = await axios.post('http://localhost:8000/analyze', {
          url: this.inputUrl,
        });
        this.urls = response.data.urls;
        console.log(this.urls)
        this.showUrlTable = true;  // Show the UrlTable component after data is fetched
      } catch (error) {
        console.error('Error submitting URL:', error);
        this.showUrlTable = false;  // Hide UrlTable if there is an error
      }
    },
  },
};
</script>

<style>
/* Global styles if needed */
</style>
