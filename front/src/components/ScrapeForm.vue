<template>
  <div>
    <input v-model="url" placeholder="Enter URL" />
    <button @click="submitUrl">Submit</button>
    <div v-if="urls.length">
      <h2>URLs Found:</h2>
      <ul>
        <li v-for="link in urls" :key="link">{{ link }}</li>
      </ul>
      <button @click="fetchContent">Fetch Content</button>
    </div>
    <div v-if="contents">
      <h2>Content:</h2>
      <table>
        <thead>
          <tr>
            <th>URL</th>
            <th>Title</th>
            <th>Content</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(content, url) in contents" :key="url">
            <td>{{ url }}</td>
            <td>{{ content.title }}</td>
            <td>{{ content.body }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      url: '',
      urls: [],
      contents: null
    };
  },
  methods: {
    async submitUrl() {
      try {
        const response = await axios.post('http://localhost:8000/analyze', { url: this.url });
        this.urls = response.data.urls;
      } catch (error) {
        console.error('Error submitting URL:', error);
      }
    },
    async fetchContent() {
      try {
        const response = await axios.post('http://localhost:8000/scrape', this.urls);
        this.contents = response.data.contents;
      } catch (error) {
        console.error('Error fetching content:', error);
      }
    }
  }
};
</script>
