<template>
<div class="container mt-5">
  <div v-if="categories.length">
    <h2>Categories</h2>
      <ul>
        <li v-for="(category, index) in categories" :key="index">{{ category }}</li>
      </ul>
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
    categories:{
      type: Array,
      required: true,
    },
   },
   };
   
 </script>
 
 <style scoped>
 /* Add any custom styles if needed */
 </style>
 