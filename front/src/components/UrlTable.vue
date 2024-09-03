<template>
  <div class="container mt-5">
    <div v-if="parsedCategories.length">
      <h2>Identified Sub-Pages in Your URLs:</h2>
      <b-card-header
        @click="isCollapsed = !isCollapsed"
        class="d-flex justify-content-between align-items-center"
      >
        <span>The system retrieved a total of {{ urls?.length || 0 }} URLs.</span>
        <div>
          <button class="btn btn-primary btn-sm" @click="downloadCSV">
            Download CSV
          </button>
          <button class="btn btn-secondary btn-sm" @click="scrapeAllUrls">
            Scrape All URLs
          </button>
          <b-button
            v-b-toggle.collapse-urls
            variant="link"
            class="text-decoration-none"
          >
            {{ isCollapsed ? "Expand" : "Collapse" }}
          </b-button>
        </div>
      </b-card-header>
      <!-- Display the table with Category and URL -->
      <table class="table table-striped">
        <thead>
          <tr>
            <th>SN.</th>
            <th>Category</th>
            <th>URL</th>
          </tr>
        </thead>
        <tbody>
          <!-- Loop through each URL entry and display it in the table -->
          <tr v-for="(item, index) in parsedCategories" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ item.category }}</td>
            <td>
              <a :href="item.url" target="_blank" rel="noopener noreferrer">{{ item.url }}</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else>
      <p>No categories found.</p>
    </div>
  </div>
</template>

<script>
import { saveAs } from 'file-saver';
import axios from 'axios'; // Make sure axios is installed and configured

export default {
  name: 'UrlTable',
  props: {
    urls: {
      type: Array,
      default: () => [], // Ensure urls is always an array
    },
  },
  data() {
    return {
      isCollapsed: true, // Track collapse state
    };
  },
  computed: {
    // Compute and parse categories to group and render correctly
    parsedCategories() {
      // Ensure data is handled safely to avoid undefined errors
      return (
        this.urls?.map((url) => ({
          category: url.category || 'Unknown Category',
          url: url.url || 'Unknown URL', // Fallback in case of missing URL
        })) || []
      ); // Default to an empty array if urls is not defined
    },
  },
  methods: {
    downloadCSV() {
      const csvContent = this.urls
        ?.map((url, index) => `${index + 1},${url.category},${url.url}`)
        .join('\n');
      const blob = new Blob([`Index,Category,URL\n${csvContent}`], {
        type: 'text/csv;charset=utf-8;',
      });
      saveAs(blob, 'unique_links.csv');
    },
    async scrapeAllUrls() {
      try {
        const response = await axios.post('/scrape-all-urls', {
          urls: this.urls.map((url) => url.url),
        });

        // Trigger file download upon successful scraping
        const blob = new Blob([JSON.stringify(response.data)], {
          type: 'application/json;charset=utf-8;',
        });
        saveAs(blob, 'output.json');
      } catch (error) {
        console.error('Error scraping URLs:', error);
        alert('Failed to scrape URLs. Please try again.');
      }
    },
  },
};
</script>
