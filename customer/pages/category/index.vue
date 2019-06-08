<template>
  <section>
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">homepage</el-breadcrumb-item>
      <el-breadcrumb-item>promotion management</el-breadcrumb-item>
      <el-breadcrumb-item>promotion list</el-breadcrumb-item>
      <el-breadcrumb-item>promotion detail</el-breadcrumb-item>
    </el-breadcrumb>
    <h1>全ての代行業一覧</h1>
    <el-row :gutter="12">
      <el-col :span="8">
        <el-card shadow="always">
          <a @click="$router.push({name:'category-yuyuid'})">家事代行</a>
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="always">
          育児代行
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="always">
          掃除代行
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="always">
          墓参り代行
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="always">
          買い物代行
        </el-card>
      </el-col>
      <el-col :span="8">
        <el-card shadow="always">
          叱り代行
        </el-card>
      </el-col>
    </el-row>
  </section>
</template>

<script>
  export default {
  data() {
    return {
      tableData: [{
        date: '家事代行',
        name: 'あなたの代わりに家事を行います',
        address: '¥ 2500~5000'
      }, {
        date: '育児代行',
        name: 'あなたの代わりに家事を行います',
        address: '¥ 2500~5000'
      }, {
        date: '掃除代行',
        name: 'あなたの代わりに家事を行います',
        address: '¥ 2500~5000'
      }, {
        date: 'お墓参り代行',
        name: 'あなたの代わりに家事を行います',
        address: '¥ 2500~5000'
      }]
    }
  }
}
</script>

<style>
</style>
