<template>
   <div>
     <h1>Website Scraper</h1>
     <input v-model="url" placeholder="Enter website URL" />
     <button @click="analyzeWebsite">Analyze</button>
 
     <div v-if="dataCategories.length">
       <h2>Data Categories</h2>
       <ul>
         <li v-for="(category, index) in dataCategories" :key="index">
           <a href="#" @click.prevent="showSample(category)">{{ category }}</a>
         </li>
       </ul>
     </div>
 
     <div v-if="sampleData.length">
       <h3>Sample Data from {{ selectedCategory }}</h3>
       <ul>
         <li v-for="(item, index) in sampleData" :key="index">{{ item }}</li>
       </ul>
       <button @click="downloadData">Download Data</button>
     </div>
   </div>
 </template>
 
 <script>
 import axios from 'axios';
 
 export default {
   data() {
     return {
       url: '',
       dataCategories: [],
       sampleData: [],
       selectedCategory: ''
     };
   },
   methods: {
     async analyzeWebsite() {
       try {
         const response = await axios.post('http://localhost:8000/analyze', { url: this.url });
         this.dataCategories = Object.keys(response.data);
       } catch (error) {
         console.error(error);
       }
     },
     async showSample(category) {
       this.selectedCategory = category;
       try {
         const response = await axios.post('http://localhost:8000/analyze', { url: this.url });
         this.sampleData = response.data[category].slice(0, 5);  // Show a sample of 5 items
       } catch (error) {
         console.error(error);
       }
     },
     async downloadData() {
       try {
         const response = await axios.post(`http://localhost:8000/download/${this.selectedCategory}`, { url: this.url });
         const link = document.createElement('a');
         link.href = `http://localhost:8000/${response.data.filename}`;
         link.download = response.data.filename;
         document.body.appendChild(link);
         link.click();
         document.body.removeChild(link);
       } catch (error) {
         console.error(error);
       }
     }
   }
 };
 </script>
 
 <style scoped>
 /* Add some basic styling */
 </style>
 