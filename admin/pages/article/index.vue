<template>
  <section>
    <el-button type="danger"><a @click="$router.push({name:'article-add'})">add Article</a></el-button>
    <table>
      <tbody>
        <tr v-for="article in articles" :key="article.id">
          <td>{{article.title}}</td>
          <td><img :src="article.image" class="card-img-top" ></td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script>
  export default{
    data() {
      return {
        articles: [],
      }
    },
    mounted() {
      this.fetchData()
    },
    methods: {
      async fetchData() {
        let res = await this.$axios.$get('article/')
        this.articles = res
      }
    }
  }
</script>
<style>
  .recipe-card {
      box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
  }
</style>
