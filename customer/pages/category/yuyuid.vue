<template>
  <section>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">homepage</el-breadcrumb-item>
      <el-breadcrumb-item>promotion management</el-breadcrumb-item>
      <el-breadcrumb-item>promotion list</el-breadcrumb-item>
      <el-breadcrumb-item>promotion detail</el-breadcrumb-item>
    </el-breadcrumb>
    <h1>家事代行</h1>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>家事代行について</span>
      </div>
      <div v-for="o in 1" :key="o" class="text item">
        {{'家事代行・家政婦を料金や相場、口コミで比較し、オンラインで予約することができます。忙しいあなたにも、たまにはちょっと楽したいあなたにも。掃除や洗濯、料理などの家事を、プロの家政婦さんにお任せしましょう！' }}
      </div>
    </el-card>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>家事代行の相場</span>
      </div>
      <div v-for="o in 1" :key="o" class="text item">
        {{'1時間3000円〜5000円' }}
      </div>
    </el-card>
    <h3>絞り込み</h3>
    <el-table
      :data="tableData"
      border
      style="width: 100%">
      <el-table-column
        prop="date"
        label="Area"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="Price"
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="Review">
      </el-table-column>
    </el-table>
    <h3>家事代行５件〜１３件</h3>
    <el-card class="box-card">
      <div slot="header" class="clearfix">
        <span>casy</span>
      </div>
      <div v-for="o in 1" :key="o" class="text item">
        {{'家事代行 23区内出張費/交通費無料 調理師免許有 ご新規様はご紹介のみ受付中' }}
        <el-button><a @click="$router.push({name:'company'})">料金と口コミを確認</a></el-button>
      </div>
    </el-card>
  </section>
</template>

<script>
  export default {
  data() {
    return {
      tableData: [{
        date: '渋谷',
        name: '¥2000~5000',
        address: '★３以上'
      },]
    }
  }
}
</script>

<style>
</style>
