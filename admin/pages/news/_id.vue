<template>
  <section>
    <h3>記事詳細</h3>
    <table>
      <tbody>
        <tr>
          <td>{{newses.title}}</td>
        </tr>
        <tr>
          <td><img :src="newses.image" class="card-img-top" ></td>
        </tr>
        <tr>
          <!-- <td>{{newses.text}}</td> -->
          <td>
            <div v-html="newses.text"></div>
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
        newses: [],
      }
    },
    mounted() {
      this.fetchData()
    },
    methods: {
      async fetchData() {
        let res = await this.$axios.$get('news/'+encodeURIComponent(this.$route.params.id)+'/')
        this.newses = res
      }
    }
  }
</script>

<style>
  .card-img-top {
    width:1000px;
  }
</style>
