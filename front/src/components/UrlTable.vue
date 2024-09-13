<template>
  <div class="container mt-5">
    <!-- Loading spinner -->
    <div v-if="isLoading" class="text-center mb-3">
      <div class="spinner-border" role="status">
        <span class="sr-only">/_\</span>
      </div>
      <p>Scraping contents within the category is in progress</p>
    </div>

    <!-- Main content -->
    <div v-if="parsedCategories.length">
      <h2>Identified Sub-Pages in Your URLs:</h2>
      <b-card-header
        @click="isCollapsed = !isCollapsed"
        class="d-flex justify-content-between align-items-center"
      >
        <span>The system retrieved a total of {{ urls?.length || 0 }} URLs.</span>
        <div>
          <button class="btn btn-primary btn-sm" @click="downloadCSV" :disabled="isScraping">
            Download CSV
          </button>
          <button class="btn btn-success btn-sm ml-2" @click="scrapeAllUrls" :disabled="isScraping">
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
            <th>Action</th>
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
            <td>
              <button class="btn btn-info btn-sm" @click="scrapeUrlContent(item.url)" :disabled="isScraping">
                Scrape Content
              </button>
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
      isLoading: false, // Track loading state
      isScraping: false, // Track scraping state to disable buttons
    };
  },
  computed: {
    // Compute and parse categories to group and render correctly
    parsedCategories() {
      // Ensure data is handled safely to avoid undefined errors
      return this.urls?.map(url => ({
        category: url.category || 'Unknown Category',
        url: url.url || 'Unknown URL', // Fallback in case of missing URL
      })) || []; // Default to an empty array if urls is not defined
    },
  },
  methods: {
    downloadCSV() {
      const csvContent = this.urls
        ?.map((url, index) => `${index + 1},${url.category},${url.url}`)
        .join('\n');
      const blob = new Blob(
        [`Index,Category,URL\n${csvContent}`],
        { type: 'text/csv;charset=utf-8;' }
      );
      saveAs(blob, 'unique_links.csv');
    },
    async scrapeAllUrls() {
      this.isScraping = true; // Disable buttons and show loading spinner
      this.isLoading = true; // Show the loading spinner
      try {
        const response = await fetch('http://localhost:8000/scrape-all-urls/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ urls: this.urls }),
        });

        if (!response.ok) throw new Error('Network response was not ok.');

        const blob = await response.blob();
        const filename = 'output.json';
        saveAs(blob, filename);
      } catch (error) {
        console.error('Error:', error);
      } finally {
        this.isScraping = false; // Enable buttons after scraping
        this.isLoading = false; // Hide the loading spinner
      }
    },
    async scrapeUrlContent(url) {
      this.isScraping = true; // Disable buttons and show loading spinner
      this.isLoading = true; // Show the loading spinner
      try {
        const response = await fetch('http://localhost:8000/scrape-unique-links-in-categories/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ urls: [url] }),  // Send only the specific URL
        });

        if (!response.ok) throw new Error('Network response was not ok.');

        const blob = await response.blob();
        const filename = 'scraped_content.json';
        saveAs(blob, filename);
      } catch (error) {
        console.error('Error:', error);
      } finally {
        this.isScraping = false; // Enable buttons after scraping
        this.isLoading = false; // Hide the loading spinner
      }
    },
  },
};
</script>

<style scoped>
.table {
  width: 100%;
  margin-top: 20px;
}

.table th,
.table td {
  text-align: left;
  padding: 8px;
}

.table th {
  background-color: #f2f2f2;
}

.table-striped tbody tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}

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
