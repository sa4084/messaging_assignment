<template>
    <div class="tasks_container">
        <div class="tasks_content">
            <h1>Tasks</h1>
            <ul class="tasks_list">
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                // tasks
                tasks: ['']
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch tasks
                    const response = await this.$http.get('http://localhost:8000/api/');
                    // set the data returned as tasks
                    this.tasks = response.data; 
                    console.log(response)
                } catch (error) {
                    // log the error
                    console.log("error")
                    console.log(error);
                }
            },
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>