<template>
  <v-text-field 
    solo
    label="Text"
    @input="searchArrayFilter()"
    type="text"
    v-model="search.text"
    >
  </v-text-field>

</template>

<script>
import Course from './Course';

export default {
    components:{
        Course
    },
    created(){
        this.searched_departments=this.departments
    },
        props:[result],
    data(){

        return{
            // This is the list of all departments so we can filter to search_departments
            departments:[
                "A E - Aerospace Engineering",
                "A M - Applied Mechanics",
                "A/R - Admissions and Records",
                "AAS - Asian American Studies",
                "ACCT - Accounting",    
                "AIS - American Indian Studies Program",
                "ANTH - Anthropology",
                "ART - Arts",
                "COMP - Computer Science",
                "CIT - Computer Information Technology", 
            ],
            // searched_departments is what will be shown to the user based on the search bar input
            searched_departments:[
            ],
            search:{
                filter: null,
                text:    ''
            }
        }
    },
    methods:{
        // This gets called when any input is put into the search bar
        searchArrayFilter(){
            console.log(this.search.text)
            var inside = this
            this.searched_departments=this.departments.filter(checkSearch)

            function checkSearch(department){
                    if(
                        department.
                        toLowerCase()
                        .indexOf(inside.search.text.toLowerCase()) != "-1"
                        // This just checks to see if our search text matches with any depatments on the list.
                        // This means if any part of a string matches the search then it will be shown. 
                    ){
                        console.log(department)
                        return department
                    }
            }

            this.searched_departments=this.searched_departments.sort(function(a,b) {
                if(a.toLowerCase().indexOf(inside.search.text.toLowerCase()) < b.toLowerCase().indexOf(inside.search.text.toLowerCase())){
                    return -1;
                }
                if(a.toLowerCase().indexOf(inside.search.text.toLowerCase()) > b.toLowerCase().indexOf(inside.search.text.toLowerCase())){
                    return 1;
                }
                if(a.toLowerCase().indexOf(inside.search.text.toLowerCase()) == b.toLowerCase().indexOf(inside.search.text.toLowerCase())){
                    return 0;
                }
            }); 
            this.$emit(searchArrayFilter(),this.searched_departments);
        }
    }
}
</script>

<style>

</style>
