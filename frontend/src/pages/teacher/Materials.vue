<script lang="ts">
export const description = "Teacher materials listing page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref, computed } from "vue";

import AppSidebar from "@/components/sidebars/AppSidebar.vue";
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar";

import {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb";

import { Separator } from "@/components/ui/separator";

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card";

import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Input } from "@/components/ui/input";
import {
  Select,
  SelectTrigger,
  SelectContent,
  SelectItem,
  SelectValue,
} from "@/components/ui/select";

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table";

import {
  BookOpen,
  Download,
  FileText,
  Folder,
  Eye,
  UploadCloud,
} from "lucide-vue-next";

const userRole = "Teacher";

// Filters
const subjectFilter = ref("");
const sectionFilter = ref("");
const search = ref("");

// Dummy materials
const materials = ref([
  {
    id: 1,
    title: "Module 1 - Introduction to Biology",
    subject: "Science",
    section: "STEM 11 - A",
    date: "2025-02-10",
    size: "1.2 MB",
    type: "PDF",
  },
  {
    id: 2,
    title: "Essay Writing Guide",
    subject: "English",
    section: "HUMSS 12 - B",
    date: "2025-02-11",
    size: "850 KB",
    type: "DOCX",
  },
  {
    id: 3,
    title: "Basic Accounting Lecture",
    subject: "Math",
    section: "ABM 12 - A",
    date: "2025-02-09",
    size: "12 MB",
    type: "PPTX",
  },
]);

const filteredMaterials = computed(() => {
  return materials.value.filter((m) => {
    const matchSubject = subjectFilter.value
      ? m.subject === subjectFilter.value
      : true;
    const matchSection = sectionFilter.value
      ? m.section === sectionFilter.value
      : true;
    const matchSearch = search.value
      ? m.title.toLowerCase().includes(search.value.toLowerCase())
      : true;

    return matchSubject && matchSection && matchSearch;
  });
});
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/dashboard">Teacher</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Materials</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Page Header -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Learning Materials</h2>
            <p class="text-sm text-muted-foreground">
              Manage uploaded modules, worksheets, and lesson files.
            </p>
          </div>

          <Button as-child class="gap-2">
            <a href="/teacher/materials/upload">
              <UploadCloud class="h-4 w-4" />
              Upload Material
            </a>
          </Button>
        </div>

        <!-- Summary Cards -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          <Card class="border-l-4 border-l-blue-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">
                Total Materials
              </CardTitle>
              <Folder class="h-5 w-5 text-blue-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">{{ materials.length }}</p>
              <p class="text-xs text-muted-foreground">Uploaded files</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-green-500">
            <CardHeader class="flex flex-row items-center justify-between pb-2">
              <CardTitle class="text-sm font-medium">
                Most Uploaded Subject
              </CardTitle>
              <BookOpen class="h-5 w-5 text-green-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">Science</p>
              <p class="text-xs text-muted-foreground">Based on material count</p>
            </CardContent>
          </Card>
        </div>

        <!-- Filters -->
        <Card>
          <CardHeader>
            <CardTitle>Filters</CardTitle>
            <CardDescription>
              Filter materials by subject, section, or keyword.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <!-- Subject Filter -->
              <Select v-model="subjectFilter">
                <SelectTrigger>
                  <SelectValue placeholder="Select Subject" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="Math">Math</SelectItem>
                  <SelectItem value="English">English</SelectItem>
                  <SelectItem value="Science">Science</SelectItem>
                </SelectContent>
              </Select>

              <!-- Section Filter -->
              <Select v-model="sectionFilter">
                <SelectTrigger>
                  <SelectValue placeholder="Select Section" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="STEM 11 - A">STEM 11 - A</SelectItem>
                  <SelectItem value="ABM 12 - A">ABM 12 - A</SelectItem>
                  <SelectItem value="HUMSS 12 - B">HUMSS 12 - B</SelectItem>
                </SelectContent>
              </Select>

              <!-- Search -->
              <Input v-model="search" placeholder="Search material..." />
            </div>
          </CardContent>
        </Card>

        <!-- Materials Table -->
        <Card>
          <CardHeader>
            <CardTitle>Uploaded Materials</CardTitle>
            <CardDescription>
              View, download, or manage learning materials.
            </CardDescription>
          </CardHeader>

          <CardContent>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Title</TableHead>
                  <TableHead>Subject</TableHead>
                  <TableHead>Section</TableHead>
                  <TableHead class="text-center">Type</TableHead>
                  <TableHead class="text-center">Size</TableHead>
                  <TableHead class="text-center">Date</TableHead>
                  <TableHead class="text-center">Actions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="m in filteredMaterials"
                  :key="m.id"
                  class="hover:bg-muted/50 cursor-pointer"
                >
                  <TableCell class="font-medium">
                    {{ m.title }}
                  </TableCell>

                  <TableCell>
                    <Badge variant="secondary">{{ m.subject }}</Badge>
                  </TableCell>

                  <TableCell>{{ m.section }}</TableCell>

                  <TableCell class="text-center">{{ m.type }}</TableCell>
                  <TableCell class="text-center">{{ m.size }}</TableCell>
                  <TableCell class="text-center">{{ m.date }}</TableCell>

                  <TableCell class="flex items-center justify-center gap-2">
                    <Button size="icon" variant="outline">
                      <Eye class="h-4 w-4" />
                    </Button>

                    <Button size="icon" variant="outline">
                      <Download class="h-4 w-4" />
                    </Button>
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
