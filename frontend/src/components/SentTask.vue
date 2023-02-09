<template>
  <div class="hello">
<div class="rows">

    <div class="todo">
      <div class="card" v-for="task in $store.state.sent"> <!-- Loop through the tasks array, if status is 'todo' then we'll show it. -->
        <div class="card-content" data_id="{{$task->id}}">
          <div class="content">
            {{ task.sender }}
            <br>
            {{ task.recipent }} <br>
            {{ task.title }} <br>
            {{ task.message }} <br>
          <button v-on:click="select(task.id)">🗑️</button> <br>

          </div>
        </div>
      </div>
    </div>
</div>
  </div>

</template>

<script>
  let user = localStorage.getItem('email');
  export default {
    // data() {
    //   return {
    //     data: [],
    //   };
    // },
    methods: {
      // async sleep(ms) {
      // setTimeout(this.fetchData(), 5000);
      // },  
      async fetchData() {      
        let response = await fetch("http://localhost:8000/api/sent/"+user); 
        let json_data =  await response.json();
        this.$store.commit('setSent',json_data)
        // this.$store.state.sent = await response.json();
      },
      select: async function(id) {
        console.log(id);
            let abc = await fetch("http://localhost:8000/api/delete_event/"+id).then(location.reload());
        },
    },
    mounted() {
      this.fetchData();
    },
  };
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
