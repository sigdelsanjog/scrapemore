<template>
  <div id="app" class="container mt-5">
    <!-- Input and Submit Button -->
    <div class="mb-3">
      <input v-model="inputUrl" type="text" class="form-control" placeholder="Enter URL" />
      <button @click="submitUrl" class="btn btn-primary mt-2">Submit</button>
    </div>

    <!-- Loading Spinner -->
    <div v-if="isLoading" class="text-center mb-3">
      <div class="spinner-border" role="status">
        <span class="sr-only"></span>
      </div>
      <p>We are analyzing the Url and fetching the web contents...</p>
    </div>

    <!-- Conditionally render UrlTable component -->
    <UrlTable v-if="!isLoading && showUrlTable" :urls="urls" :categories="categories" :pages="pages" />
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
      categories: [],
      pages: [],
      showUrlTable: false,
      isLoading: false,  // Track loading state
    };
  },
  methods: {
    async submitUrl() {
      if (!this.inputUrl) {
        alert('Please enter a URL.');
        return;
      }
      this.isLoading = true; // Show the loading spinner
      this.showUrlTable = false; // Hide the UrlTable component during loading

      try {
        const response = await axios.post('http://localhost:8000/analyze', {
          url: this.inputUrl,
        });
        this.urls = response.data.urls;
        this.categories = response.data.categories;
        this.pages = response.data.pages;
        this.showUrlTable = true;  // Show the UrlTable component after data is fetched
      } catch (error) {
        console.error('Error submitting URL:', error);
        this.showUrlTable = false;  // Hide UrlTable if there is an error
      } finally {
        this.isLoading = false; // Hide the loading spinner
      }
    },
  },
};
</script>

<style>
/* Global styles if needed */
.spinner-border {
  width: 3rem;
  height: 3rem;
  border-width: 0.4em;
}
.spinner-border-sm {
  width: 2rem;
  height: 2rem;
  border-width: 0.3em;
}
</style>
