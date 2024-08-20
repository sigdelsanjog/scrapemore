<template>
   <div>
     <h2>Scraped Data</h2>
     <div v-if="data.Images.length">
       <h3>Images</h3>
       <ul>
         <li v-for="img in data.Images" :key="img">{{ img }}</li>
       </ul>
     </div>
 
     <div v-if="data.Links.length">
       <h3>Links</h3>
       <ul>
         <li v-for="link in data.Links" :key="link">{{ link }}</li>
       </ul>
     </div>
 
     <div v-if="data.Headings.h1.length">
       <h3>Headings (H1)</h3>
       <ul>
         <li v-for="heading in data.Headings.h1" :key="heading">{{ heading }}</li>
       </ul>
     </div>
 
     <div v-if="data.Paragraphs.length">
       <h3>Paragraphs</h3>
       <ul>
         <li v-for="paragraph in data.Paragraphs" :key="paragraph">{{ paragraph }}</li>
       </ul>
     </div>
   </div>
 </template>
 
 <script>
 export default {
   props: ['data']
 }
 </script>
 