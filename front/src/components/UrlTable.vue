<template>
<div class="container mt-5">
  <div v-if="categories.length">
  <h2>Categories</h2>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Category</th>
            <th>Link</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(category, index) in categories" :key="index">
            <td>{{ category.category }}</td>
            <td><a :href="category.link" target="_blank">{{ category.link }}</a></td>
          </tr>
        </tbody>
      </table>
      </div>
      <div v-else>
        <p>No categories found.</p>
      </div>
     <h2>URL Links</h2>
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
  </div>

 </template>
 
 <script>
export default {
  name: 'UrlTable',
    props: {
      urls:{
        type: Array,
        required:true,
      },
    },
  data() {
    return {
      categories: []
    };
  },
  methods: {
    async fetchCategories() {
      try {
        const response = await fetch("http://localhost:8000/analyze", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            url: "https://example.com",
            domain: "https://thequickblog.com"
          })
        });
        const data = await response.json();
        this.categories = data.categories;
      } catch (error) {
        console.error("Error fetching categories:", error);
      }
    }
  },
  mounted() {
    this.fetchCategories();
  }
};
</script>

<style scoped>
.table {
  width: 100%;
  margin-top: 20px;
}

.table th, .table td {
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