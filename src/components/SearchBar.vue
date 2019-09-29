<template>
<v-app>
  <v-text-field 
    solo
    label="Text"
    @input="searchArrayFilter()"
    type="text"
    v-model="search.text"
    >
  </v-text-field>
  <v-card v-for="department in searched_departments" :key=department.id>
      <!-- insert course component here -->
            {{department}}
  </v-card>
</v-app>
</template>

<script>
export default {
    created(){
        this.searched_departments=this.departments
    },
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
        }
    }
}
</script>

<style>

</style>