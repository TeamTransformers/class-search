<template>
<div>
    <div 
    v-for="data in abbr"
    :key = data
    >
    {{"https://api.metalab.csun.edu/curriculum/api/2.0/courses/"+data}}
    </div>    
</div>
</template>

<script>
import abbrv from "../python/abbrv.json";
export default {
  data() {
    return {
        abbr: abbrv
    }
  },
};
</script>

<style>
</style>