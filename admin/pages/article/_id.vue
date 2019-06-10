<template>
  <section>
    <h3>記事詳細</h3>
    <table>
      <tbody>
        <tr>
          <td>{{articles.title}}</td>
        </tr>
        <tr>
          <td><img :src="articles.image" class="card-img-top" ></td>
        </tr>
        <tr>
          <!-- <td>{{articles.text}}</td> -->
          <td>
            <div v-html="articles.text"></div>
          </td>
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
        let res = await this.$axios.$get('article/'+encodeURIComponent(this.$route.params.id)+'/')
        this.articles = res
      }
    }
  }
</script>

<style>
  .card-img-top {
    width:1000px;
  }
</style>
