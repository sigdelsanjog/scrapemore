<template>
  <div class="container mt-5">
    <div v-if="categories.length || pages.length">
      <h2>We identified the following sub-pages existing in your URLs:</h2>
      <div v-if="pages.length">
        <h3>Pages</h3>
        <table>
          <thead>
            <tr>
              <th>Page</th>
              <th>URL</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(page, index) in pages" :key="index">
              <td>{{ page.category }}</td>
              <td><a :href="page.link" target="_blank">{{ page.link }}</a></td>
            </tr>
          </tbody>
        </table>
      </div>
      <h2>Categories</h2>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Category</th>
            <th>Link</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(categoryObj, index) in categories" :key="index">
            <td>{{ categoryObj.category }}</td>
            <td><a :href="categoryObj.link" target="_blank">{{ categoryObj.link }}</a></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else>
      <p>No categories found.</p>
    </div>

    <!-- Collapsible section for URL Links -->
    <b-card no-body class="mt-4">
      <b-card-header @click="isCollapsed = !isCollapsed" class="d-flex justify-content-between align-items-center">
        <span>The system retrieved a total of {{ urls.length }} URLs.</span>
        <div>
          <button class="btn btn-primary btn-sm" @click="downloadCSV">Download CSV</button>
          <b-button v-b-toggle.collapse-urls variant="link" class="text-decoration-none">
            {{ isCollapsed ? 'Expand' : 'Collapse' }}
          </b-button>
        </div>
      </b-card-header>
      <b-collapse id="collapse-urls" v-model="isCollapsed">
        <b-card-body>
          <table class="table table-striped" v-if="urls.length">
            <thead>
              <tr>
                <th>#</th>
                <th>URL</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(url, index) in urls" :key="index">
                <td>{{ index + 1 }}</td>
                <td>
                  <a :href="url" target="_blank" rel="noopener noreferrer">{{ url }}</a>
                </td>
              </tr>
            </tbody>
          </table>
          <p v-else>No URLs found.</p>
        </b-card-body>
      </b-collapse>
    </b-card>
  </div>
</template>

<script>
import { saveAs } from 'file-saver';

export default {
  name: 'UrlTable',
  props: {
    categories: {
      type: Array,
      default: () => [],
    },
    pages: {
      type: Array,
      default: () => [],
    },
    labels: {
      type: Array,
      default: () => [],
    },
    urls: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      isCollapsed: true, // Track collapse state
    };
  },
  methods: {
    downloadCSV() {
      const csvContent = this.urls.map((url, index) => `${index + 1},${url}`).join('\n');
      const blob = new Blob([`# URL List\nIndex,URL\n${csvContent}`], { type: 'text/csv;charset=utf-8;' });
      saveAs(blob, 'unique_links.csv');
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
</style>
