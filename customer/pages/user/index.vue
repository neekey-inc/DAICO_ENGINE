<template>
  <div>
    <el-breadcrumb>
      <el-breadcrumb-item><a @click="$router.push({name:'user'})">マイページ</a></el-breadcrumb-item>
      <el-breadcrumb-item><a @click="$router.push({name:'user-mypage-message'})">メッセージ</a></el-breadcrumb-item>
      <el-breadcrumb-item><a @click="$router.push({name:'user-mypage-manage'})">予約管理</a></el-breadcrumb-item>
      <el-breadcrumb-item><a @click="$router.push({name:'user-mypage-quote'})">仮予約</a></el-breadcrumb-item>
      <el-breadcrumb-item><a @click="$router.push({name:'user-mypage-account'})">登録内容</a></el-breadcrumb-item>
      <el-breadcrumb-item></el-breadcrumb-item>
    </el-breadcrumb>
  <h2>マイページ</h2>
  <div>
    <el-divider content-position="left">未読メッセージ　<el-link @click="$router.push({name:'user-mypage-message'})">一覧</el-link></el-divider>
    <el-form>

    </el-form>
    <el-divider content-position="left">予約 <el-link @click="$router.push({name:'user-mypage-manage'})">一覧</el-link></el-divider>
    <el-form>

    </el-form>
    <el-divider content-position="left">仮予約 <el-link @click="$router.push({name:'user-mypage-quote'})">一覧</el-link></el-divider>
    <el-form>

    </el-form>
  </div>
</div>

</template>
